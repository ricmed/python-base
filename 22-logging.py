#!/usr/bin/env python3
"""Criação de log
"""

import os
import logging
from logging.handlers import RotatingFileHandler  # Rotaciona o arquivo de log

log_level = os.getenv('LOG_LEVEL', 'DEBUG').upper()
log = logging.Logger('logs.py', log_level)
# File handler
fh = RotatingFileHandler('app.log', maxBytes=10**6, backupCount=10)
fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - l:%(lineno)d - f:%(filename)s %(message)s'
)
fh.setFormatter(fmt)
log.addHandler(fh)


log.debug('Mensagem pro desenvolvedor, QA, SysAdmin')
log.info('Mensagem geral para o usuário')
log.warning('Mensagem de alerta, não causa erro')
log.error('Mensagem de erro, afeta uma única execução')
log.critical('Mensagem de erro crítico, afeta todo o sistema')



