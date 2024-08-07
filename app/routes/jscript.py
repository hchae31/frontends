from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

# 라우터 생성
jscript_router = APIRouter()
# 템플릿 지정
templates = Jinja2Templates(directory='views/templates')

# 라우트 설정
@jscript_router.get('/hello')
async def hello(req: Request):
    return templates.TemplateResponse('js/01hello.html', {'request': req})

# 라우트 설정
@jscript_router.get('/type')
async def type(req: Request):
    return templates.TemplateResponse('js/02type.html', {'request': req})

# 라우트 설정
@jscript_router.get('/operator')
async def type(req: Request):
    return templates.TemplateResponse('js/03operator.html', {'request': req})

# 라우트 설정
@jscript_router.get('/condition')
async def type(req: Request):
    return templates.TemplateResponse('js/04condition.html', {'request': req})

# 라우트 설정
@jscript_router.get('/loop')
async def type(req: Request):
    return templates.TemplateResponse('js/05loop.html', {'request': req})

# 라우트 설정
@jscript_router.get('/array')
async def type(req: Request):
    return templates.TemplateResponse('js/06array.html', {'request': req})

# 라우트 설정
@jscript_router.get('/while')
async def type(req: Request):
    return templates.TemplateResponse('js/07while.html', {'request': req})

# 라우트 설정
@jscript_router.get('/function')
async def type(req: Request):
    return templates.TemplateResponse('js/08function.html', {'request': req})