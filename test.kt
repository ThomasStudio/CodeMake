package com.example.hscroll

import android.animation.AnimatorSet
import android.animation.ObjectAnimator
import android.content.Context
import android.graphics.Rect
import android.util.AttributeSet
import android.util.Log
import android.view.MotionEvent
import android.view.View
import android.widget.FrameLayout
import androidx.core.view.children
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

/**
 * Created by thomas on 4/15/2023.
 * layout for RecyclerView to implement horizontal pull to refresh
 *
 * only work for RecyclerView, RecyclerView.Adapter and horizontal LinearLayoutManager
 */
interface TestIF{
    val Name: String
    fun test()
}

class HScrollLayout @JvmOverloads constructor(
    context: Context, attrs: AttributeSet? = null, defStyleAttr: Int = 0
) : FrameLayout(context, attrs, defStyleAttr) {

    val TAG = "HScrollLayout"

    var animateTime = 400

    /**
     * 阻尼系数
     */
    var dampingCoefficient = 0.3f

    private var recyclerView: RecyclerView? = null
    private val original = Rect()
    private var isMoved = false
    private var xStart = 0f
    private var isSuccess = false
    private var mScrollListener: ScrollListener? = null

    //    private var canPullFooter = false
    private var footer: View? = null
    private val footerOriginal = Rect()

    //when recyclerView offset >= footerMaxGap, pull it
    var footerMaxGap = 0

    override fun onFinishInflate() {
        super.onFinishInflate()

        children.forEach {
            if (it is RecyclerView) {
                recyclerView = it
            }
        }
    }

    override fun onLayout(changed: Boolean, l: Int, t: Int, r: Int, b: Int) {
        super.onLayout(changed, l, t, r, b)

        recyclerView?.apply { original[left, top, right] = bottom }
        footer?.apply { footerOriginal[left, top, right] = bottom }
    }

    fun setScrollListener(listener: ScrollListener?) {
        mScrollListener = listener
    }

    override fun dispatchTouchEvent(ev: MotionEvent): Boolean {
        Log.d(TAG, "dispatchTouchEvent: $ev")

        if (recyclerView == null) {
            return super.dispatchTouchEvent(ev)
        }

        val xTouch = ev.x
        if (xTouch >= original.right || xTouch <= original.left) {
            if (isMoved) {
                recoverLayout()
            }
            return true
        }
        return when (ev.action) {
            MotionEvent.ACTION_DOWN -> {
                xStart = ev.x
                handleMotionEvent(ev)
            }

            MotionEvent.ACTION_MOVE -> {
                handleMotionEvent(ev)
            }

            MotionEvent.ACTION_UP -> {
                if (isMoved) {
                    recoverLayout()
                }
                !isSuccess || super.dispatchTouchEvent(ev)
            }

            else -> true
        }
    }

    /**
     * 取消子view已经处理的事件
     *
     * @param ev event
     */
    private fun cancelChild(ev: MotionEvent) {
        ev.action = MotionEvent.ACTION_CANCEL
        super.dispatchTouchEvent(ev)
    }

    /**
     * 位置还原
     */
    private fun recoverLayout() {
        recyclerView?.apply {
            val offset = this.left - original.left

            mScrollListener?.apply { onRecover(offset) }

            val anim = ObjectAnimator.ofFloat(this, "translationX", offset.toFloat(), 0f).apply {
                duration = animateTime.toLong()
            }

            anim.addUpdateListener {
                if (it.animatedValue == 0f) {
                    mScrollListener?.apply { onRecovered(offset) }
                }
            }

            val footerAnimotor = getFooterAnimator(offset)

            if (footerAnimotor == null) {
                anim.start()
            } else {
                val animSet = AnimatorSet()
                animSet.playTogether(anim, footerAnimotor)
                animSet.start()
            }

            original.let { this.layout(it.left, it.top, it.right, it.bottom) }
            footerOriginal.let { footer?.layout(it.left, it.top, it.right, it.bottom) }

            isMoved = false
        }
    }

    private fun isLastItemShowed(): Boolean {
        if (recyclerView == null || recyclerView?.adapter !is Adapter || recyclerView?.layoutManager !is LinearLayoutManager) {
            return false
        }

        return recyclerView?.let { view ->
            view.adapter?.let { adapter ->
                (view.layoutManager as LinearLayoutManager?)?.let { mgr ->
                    val itemCount = adapter.itemCount
                    val lastVisibleIndex = mgr.findLastCompletelyVisibleItemPosition()
                    (lastVisibleIndex >= (itemCount - 1))
                } ?: false
            } ?: false
        } ?: false
    }

    fun handleMotionEvent(ev: MotionEvent): Boolean {
        val scrollX = ev.x - xStart
        val pullLeft = (scrollX < 0) && isLastItemShowed()
        if (pullLeft) {
            cancelChild(ev)
            val offset = (scrollX * dampingCoefficient).toInt()

            recyclerView?.let {
                original.apply { it.layout(left + offset, top, right + offset, bottom) }
                pullFooter(-offset)
            }

            mScrollListener?.apply { onScroll(offset) }

            isMoved = true
            isSuccess = false
            return true
        } else {
            mScrollListener?.apply { onNoScroll() }

            xStart = ev.x
            isMoved = false
            isSuccess = true
            return super.dispatchTouchEvent(ev)
        }
    }

    fun setFooter(view: View) {
        footer = view
    }

    fun pullFooter(recyclerOffset: Int) {
        if (footerMaxGap == 0 || footer == null || recyclerView == null || recyclerOffset < footerMaxGap) return

        val gap = recyclerOffset - footerMaxGap

        footerOriginal.apply {
            footer!!.layout(left - gap, top, right - gap, bottom)
        }
    }

    fun getFooterAnimator(offset: Int): ObjectAnimator? {
        if (footerMaxGap == 0 || footer == null || offset == 0) return null

        return footer?.let {
            val footOffset = it.left - footerOriginal.left

            if (footOffset == 0) {
                return null
            }

            val duration = (animateTime * footOffset / offset).toLong()

            Log.d(TAG, "getFooterRecoverAnimation: $offset, $footOffset,$animateTime, $duration")

            if (duration <= 0) {
                return null
            }

            ObjectAnimator.ofFloat(it, "translationX", footOffset.toFloat(), 0f).apply {
                this.duration = duration
            }
        }
    }

    interface ScrollListener {
        fun onScroll(offset: Int)
        fun onNoScroll()
        fun onRecover(offset: Int)
        fun onRecovered(offset: Int)
    }

}