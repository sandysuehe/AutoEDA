#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-12-26 10:55:36
# File Name: template.py
# Description: 
#########################################################################
def head_cell():
    return {"cell_type": "code",
            "execution_count": 1,
            "metadata": {},
            "outputs": [],
            "source": [
                "import pandas as pd\n",
                "import pandas_profiling\n",
                "import matplotlib.pyplot as plt\n",
                "# 加上这行才能画图呢\n",
                "%matplotlib inline"
                ]
            }

def subject_cell(desc):
    return {"cell_type": "markdown",
            "metadata": {},
            "source": [desc]
            }

def loadfile_cell(dataname, filename):
    return {"cell_type": "code",
            "execution_count": 2,
            "metadata": {},
            "outputs": [],
            "source": [
                "%s = pd.read_csv(\"%s\")" % (dataname, filename)
                ]
            }

def loadfile_sep_cell(dataname, filename, sep):
    return {"cell_type": "code",
            "execution_count": 2,
            "metadata": {},
            "outputs": [],
            "source": [
                "%s = pd.read_csv(\"%s\", sep = '\%s')" % (dataname, filename, sep)
                ]
            }

def genreport_cell(dataname, html):
    return {"cell_type": "code",
            "execution_count": 27,
            "metadata": {},
            "outputs": [],
            "source": [
                "pfr = pandas_profiling.ProfileReport(%s)\n" % (dataname),
                "pfr.to_file('%s')" % html
                ]
            }

def metadata_cell():
    return {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
                },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                    },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.7.1"
                }
            }
# vim: set noexpandtab ts=4 sts=4 sw=4 :
