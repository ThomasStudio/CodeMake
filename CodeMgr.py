from enum import Enum
from importlib import import_module, reload
import copy
import os

from Util import *


class TemplateType(Enum):
    Create = 'create'
    Modify = 'modify'


class OperType(Enum):
    Replace = 'replace'
    InsertAfter = 'insertAfter'
    InsertBefore = 'insertBefore'


def getTemplate(py: str) -> dict:
    ''' get template
    '''

    py = py.replace('.py', '')

    try:
        t = import_module(py)
        reload(t)

        template: dict = t.template

        if 'type' not in template:
            return None

        if template['type'] not in ['create', 'modify']:
            return None

        return template

    except Exception as e:
        log(f'getTemplate : {e}')

    return None


def getPatt(template: dict):
    t = template['type']
    if t == TemplateType.Create.value:
        return getCreatePatt(template)
    elif t == TemplateType.Modify.value:
        return getModifyPatt(template)

    return ''


def getCreatePatt(template: dict):
    patts = []
    for x in template['files']:
        p = x['path']
        patts.append(p)

        p = x['code']
        patts.append(p+'\n')

    return '\n'.join(patts)


def getModifyPatt(template: dict):
    patts = []
    for x in template['files']:
        p = x['path']
        patts.append(p)

        for y in x['operator']:
            patts.append(f"{y['type']}")

            patts.append('-------- patt --------')
            patts.append(y['patt'])
            patts.append('\n-------- code --------')
            patts.append(y['code'])

    return '\n'.join(patts)


def build(template: dict, args: dict) -> dict:
    temp = copy.deepcopy(template)
    try:
        t = temp['type']

        if t == TemplateType.Create.value:
            return buildCreate(temp, args)
        elif t == TemplateType.Modify.value:
            return buildModify(temp, args)
    except Exception as e:
        log(f'build error: {e}')

    return None


def buildCreate(template: dict, args: dict) -> dict:
    rs = template.copy()
    for x in rs['files']:
        x['path'] = replaceArgs(x['path'], args)
        x['code'] = replaceArgs(x['code'], args)

    return rs


def buildModify(template: dict, args: dict) -> dict:
    rs = template
    for x in template['files']:
        x['path'] = replaceArgs(x['path'], args)

        for y in x['operator']:
            y['patt'] = replaceArgs(y['patt'], args)
            y['code'] = replaceArgs(y['code'], args)

    return rs


def replaceArgs(s: str, args: dict):
    rs = s

    for k in args:
        rs = rs.replace('{' + k + '}', args[k])

    return rs


def generate(template: dict, args: dict) -> bool:
    builtTemp = build(template, args)

    if builtTemp['type'] == TemplateType.Create.value:
        return generateNewFile(builtTemp)
    elif builtTemp['type'] == TemplateType.Create.value:
        return modifyFile(builtTemp)

    return False


def generateNewFile(builtTemp: dict):
    for x in builtTemp['files']:
        p = x['path']
        code = x['code']

        try:

            with open(p, 'x', encoding='utf-8') as f:
                f.write(code)

        except Exception as e:
            log(f'generateNewFile Error: {e}')
            return False

    return True


def modifyFile(code: dict):
    pass
