#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © %YEAR% %USER% <%MAIL%>
#
# Distributed under terms of the %LICENSE% license.

"""
"""

from openerp.osv import osv, fields, orm
import logging

_logger = logging.getLogger(__name__)

class %FILE%(osv.Model):
    _name = "%OPENERPCLASS%"
    _description = ""
    _columns = {
        %HERE%
    }
