#!/bin/python3
#-*- coding:utf-8 -*-
# grbh0226@gmail.com2019-08-09 10:14:17

import os
import sys
from datetime import *
import time

projectPath = os.environ["HOME"]+"/xxproject/src"
serverName = ""



def write_file(filepath,lines):
    #检测目录，不存在 mkdir
    name = os.path.basename(filepath)
    if False == os.path.exists(os.path.dirname(filepath)):
        os.makedirs(os.path.dirname(filepath))
        print("mkdir "+os.path.dirname(filepath)+" ...")

    print("gen "+filepath+" ....")
    with open(filepath,"w") as f:
        for line in lines:
            f.write(line)
    print("gen "+filepath+" done!")

def head_comment(filename):
    curr_date = datetime.fromtimestamp(time.time())
    head_comment = []
    head_comment.append("/********************************************************************************************\n")
    head_comment.append("* Copyright(c) "+str(curr_date.year)+", all rights reserved\n")
    head_comment.append("*\n")
    head_comment.append("* File:      \t\t\t\t"+filename+"\n")
    head_comment.append("* Author:\n")
    head_comment.append("* Revision:\n")
    head_comment.append("* Description:\n")
    head_comment.append("* Create:    \t\t\t\t"+curr_date.strftime("%Y-%m-%d %H:%M:%S")+"\n")
    head_comment.append("* Modified:  \t\t\t\t"+curr_date.strftime("%Y-%m-%d %H:%M:%S")+"\n")
    head_comment.append("*********************************************************************************************/\n")
    return head_comment

def single_case_class(name):
    h_lines = []
    cpp_lines = []
    # 首字母大写
    # TODO
    # 需要更加健壮
    ClassName = "C"+name[0:1].capitalize()+name[1:]
    h_lines.extend(head_comment(name+".h"))
    h_lines.append("\n")
    h_lines.append("\n")
    h_lines.append("\n")
    h_lines.append("#pragma once\n")
    h_lines.append("\n")
    h_lines.append("class "+ClassName+"\n")
    h_lines.append("{\n")
    h_lines.append("\tpublic:\n")
    h_lines.append("\t\t ~"+ClassName+"();\n")
    h_lines.append("\t\t static "+ClassName+" *GetInst();\n")
    h_lines.append("\t\t bool Init();\n")
    h_lines.append("\n")
    h_lines.append("\tprivate:\n")
    h_lines.append("\t\t "+ClassName+"();\n")
    h_lines.append("\t\t "+ClassName+"(const "+ClassName+"&) =delete;\n")
    h_lines.append("\t\t "+ClassName+"& operator=(const "+ClassName+"&) =delete;\n")
    h_lines.append("\t\t static const constexpr char * __CLASS__=\""+ClassName+"\";\n")
    h_lines.append("};\n")


    cpp_lines.extend(head_comment(name+".cpp"))
    cpp_lines.append("\n")
    cpp_lines.append("\n")
    cpp_lines.append("\n")
    cpp_lines.append("#include \""+name+".h\"\n")
    cpp_lines.append("#include <memory>\n")
    cpp_lines.append("#include <mutex>\n")
    cpp_lines.append("#include <mutex>\n")
    cpp_lines.append("\n")
    cpp_lines.append("\n")
    cpp_lines.append("\t"+ClassName+" :: "+ClassName+"()\n")
    cpp_lines.append("\t"+"{\n")
    cpp_lines.append("\t\t //TODO\n")
    cpp_lines.append("\t"+"}\n")
    cpp_lines.append("\n")
    cpp_lines.append("\t"+ClassName+" :: ~"+ClassName+"()\n")
    cpp_lines.append("\t"+"{\n")
    cpp_lines.append("\t\t //TODO\n")
    cpp_lines.append("\t"+"}\n")
    cpp_lines.append("\n")
    cpp_lines.append("\t"+ClassName+" * "+ClassName+" :: GetInst()\n")
    cpp_lines.append("\t"+"{\n")
    cpp_lines.append("\t\t static std::unique_ptr<"+ClassName+"> instance;\n")
    cpp_lines.append("\t\t static std::once_flag once;\n")
    cpp_lines.append("\t\t std::call_once (once,[&](){instance.reset(new "+ClassName+");});\n")
    cpp_lines.append("\t\t return instance.get();\n")
    cpp_lines.append("\t"+"}\n")
    cpp_lines.append("\n")
    cpp_lines.append("\tbool "+ClassName+" :: Init()\n")
    cpp_lines.append("\t"+"{\n")
    cpp_lines.append("\t\t //TODO\n")
    cpp_lines.append("\t\t return true;\n")
    cpp_lines.append("\t"+"}\n")
    return h_lines,cpp_lines

def common_class(name):
    h_lines=[]
    cpp_lines = []
    # 首字母大写
    # TODO
    # 需要更加健壮
    ClassName = "C"+name[0:1].capitalize()+name[1:]
    # ClassName = "C"+name.capitalize()
    h_lines.extend(head_comment(name+".h"))
    h_lines.append("\n")
    h_lines.append("\n")
    h_lines.append("\n")
    h_lines.append("#pragma once\n")
    h_lines.append("\n")
    h_lines.append("class "+ClassName+"\n")
    h_lines.append("{\n")
    h_lines.append("\tpublic:\n")
    h_lines.append("\t\t "+ClassName+"();\n")
    h_lines.append("\n")
    h_lines.append("\t\t ~"+ClassName+"();\n")
    h_lines.append("\n")
    h_lines.append("\tprivate:\n")
    h_lines.append("\t\t static const constexpr char * __CLASS__=\""+ClassName+"\";\n")
    h_lines.append("};\n")


    cpp_lines.extend(head_comment(name+".cpp"))
    cpp_lines.append("\n")
    cpp_lines.append("\n")
    cpp_lines.append("\n")
    cpp_lines.append("#include \""+name+".h\"\n")
    cpp_lines.append("\n")
    cpp_lines.append("\n")
    cpp_lines.append("\t"+ClassName+" :: "+ClassName+"()\n")
    cpp_lines.append("\t"+"{\n")
    cpp_lines.append("\t\t //TODO;\n")
    cpp_lines.append("\t"+"}\n")
    cpp_lines.append("\n")
    cpp_lines.append("\t"+ClassName+" :: ~"+ClassName+"()\n")
    cpp_lines.append("\t"+"{\n")
    cpp_lines.append("\t\t //TODO;\n")
    cpp_lines.append("\t"+"}\n")
    return h_lines,cpp_lines

def gen_class(name,singleCase):

    global serverName
    h_filename = name + ".h"
    cpp_filename = name + ".cpp"
    h_lines=[]
    cpp_lines= []
    h_filepath = os.path.join(projectPath,serverName,h_filename)
    cpp_filepath = os.path.join(projectPath,serverName,cpp_filename)
    if True == os.path.exists(h_filepath):
        # TODO
        print(h_filepath +" exists!!!")
        return

    if True==singleCase:
        h_lines,cpp_lines = single_case_class(name)
    else:
        h_lines,cpp_lines = common_class(name)

    if 0==len(h_lines) or 0==len(cpp_lines):
        return
    write_file(h_filepath,h_lines)
    write_file(cpp_filepath,cpp_lines)

def main(args):

    global serverName
    Usage = " ".join(("Usage: python/python3",args[0],"serverName","classname"))
    if len(args)<3:
        print(Usage)
        return
    serverName = args[1]
    print(serverName)
    classname = args[2]
    gen_class(classname,True)

if __name__ == '__main__':
    main(sys.argv)

