from django.urls import path
from  . import views

urlpatterns=[
    path('app/',views.app,name="app"),
    path('login/',views.login,name="login"),
    path('billetera/',views.billetera,name="billetera"),
    path('',views.home,name="home"),
    path('crear_cuenta/',views.crear_cuenta,name="crear_cuenta"),
    path('añadir_saldo/',views.añadir_saldo,name="añadir_saldo"),
    path('editar_medios_pagos/',views.editar_medios_pagos,name="editar_medios_pagos"),
    path('editar_saldo_usuario/',views.editar_saldo_usuario,name="editar_saldo_usuario"),
    path('editar_tarifa_envio/',views.editar_tarifa_envio,name="editar_tarifa_envio"),
]