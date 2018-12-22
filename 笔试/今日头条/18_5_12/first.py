# coding=utf-8
import sys
import re

if __name__ == "__main__":
    # 读取第一行的n
    sd = input()
    sigle_comment = re.compile("^//(\w|d)")
    begin_cooment = re.compile("/\*.*?")
    end_comment = re.compile("\*/.*?")
    line = 0
    is_in = False
    comment_line = 0
    begin_line = 0
    while sd != "":
        line += 1
        if not is_in:
            if sigle_comment.match(sd):
                comment_line += 1
            elif begin_cooment.findall(sd):
                begin_line = line
                if end_comment.findall(sd):
                    if len(begin_cooment.findall(sd)) == len(end_comment.findall(sd)):
                        comment_line += len(begin_cooment.findall(sd))
                else:
                    is_in = True
            # 在多行注释中
        else:
            if end_comment.match(sd):
                is_in = False
                comment_line += line - begin_line
        sd = input()
    print(comment_line)
