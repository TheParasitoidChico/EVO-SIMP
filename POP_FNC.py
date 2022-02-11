#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 11:10:48 2022
@author: christian
"""
import math as m
# Unbounded Growth
def unbounded_growth(n,r,t,):
    e = m.e
    pop = n*e**(r*t)
    return(pop)
# growth rates considering death rates
def grw_n_die_rate(n,r,d):
    rate = (r-d)*n
    return(rate)
def popexpn_K(n,r,K):
    rate = r*n*(1-(n/K))
    return(rate)
def popK_at_time(n,r,t,K):
    e=m.e
    cu = K*n*(e**(r*t))
    k = (e**(r*t))-1
    nt = (cu/(K+(n*k)))
    return(nt)
