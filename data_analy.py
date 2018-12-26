#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-12-25 19:01:14
# File Name: dataanaly.py
# Description: 生成EDA分析的代码
#########################################################################
import os
import sys
import getopt
import json
import template
def get_filename(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # root: 当前目录路径
        # dirs: 当前路径下所有子目录
        # files: 当前路径下所有非目录子文件
        return root, files

def deal_csv(cur_dir, filename, cells_array):
    filepath = "{0}/{1}".format(cur_dir, filename)
    dataname = filename.replace(".csv", "")
    cells_array.append(template.subject_cell("# 分析数据集{0}".format(filename)))
    cells_array.append(template.loadfile_cell(dataname, filepath)) 
    cells_array.append(template.genreport_cell(dataname, "{0}.html".format(dataname)))

def deal_common(cur_dir, filename, content, sep):
    filepath = "{0}/{1}".format(cur_dir, filename)
    dataname = filename.replace(".csv", "")
    cells_array.append(template.subject_cell("# 分析数据集{0}".format(filename)))
    cells_array.append(template.loadfile_sep_cell(dataname, filepath, sep)) 
    cells_array.append(template.genreport_cell(dataname, "{0}.html".format(dataname)))

def generate_ipb(cur_dir, datafile_list):
    cells_array = [template.head_cell()]
    for datafile in datafile_list:
        if datafile.endswith('.csv'):
            deal_csv(cur_dir, datafile, cells_array)
        else:
            deal_common(cur_dir, datafile, cells_array, sep)
    return {
            "cells": cells_array,
            "metadata": template.metadata_cell(), 
            "nbformat": 4,
            "nbformat_minor": 2
            } 

def write_ipb(content):
    with open('AutoGen.ipynb', 'w') as fileipb:
        fileipb.write(json.dumps(content))
        fileipb.close()

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hd:s:",["dataset=","sep="])
    except getopt.GetoptError:
        print 'data_analy.py -d <dataset> -s <sep>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'data_analy.py -d <dataset> -s <sep>'
            sys.exit()
        elif opt in ("-d", "--dataset"):
            dataset = arg
        elif opt in ("-s", "--sep"):
            sep = arg
    print "数据集目录：", dataset 
    print "数据分隔符：", sep 

    print "开始生成EDA分析代码......"
    cur_dir, datafile_list = get_filename(dataset)
    ipb = generate_ipb(cur_dir, datafile_list)
    write_ipb(ipb)
    print "已生成EDA分析代码，生成文件在当前目录: {0}/AutoGen.ipynb".format(os.getcwd())

if __name__=='__main__':
    main(sys.argv[1:])
# vim: set noexpandtab ts=4 sts=4 sw=4 :
