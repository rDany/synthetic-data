#!/bin/python
import re

class data_compiler():
    reduce_result = []
    human_input = []
    robot_output = []
    txt_input = ''
    txt_output = ''
    
    def reduce_msg(self, text):
        mit = re.finditer(r'\[(.+?)\]', text)
        any_ = False
        for m in mit:
            any_ = True
            text_out = ''
            inside_text = text[m.start(1):m.end(1)]
            half_a = text[:m.start(1)-1]
            half_b = text[m.end(1)+1:]
            
            mcit = re.split(r'\|', inside_text)
            if len(mcit) == 1:
                text_out = half_a + half_b
                if not re.search(r'\[', text_out):
                    if not text_out in self.reduce_result:
                        self.reduce_result.append(text_out)
                else:
                    self.reduce_msg(text_out)
                text_out = half_a + mcit[0] + half_b
                if not re.search(r'\[', text_out):
                    if not text_out in self.reduce_result:
                        self.reduce_result.append(text_out)
                else:
                    self.reduce_msg(text_out)
            else:
                for mc in mcit:
                    text_out = half_a + mc + half_b
                    if not re.search(r'\[', text_out):
                        self.reduce_result.append(text_out)
                    else:
                        self.reduce_msg(text_out)
        if not any_:
            self.reduce_result.append(text)

    def compile(self, file_name):
        with open(file_name, 'r') as f:
            rdany_data = f.readlines()
        f.closed
        prev = 'robot'
        
        count = 0
        rdany_data.append([])
        for data in rdany_data:
            count += 1
            data = data[:-1]
            if len(data) < 1:
                if prev == 'robot' and len(self.human_input) > 0 and len(self.robot_output) > 0:
                    for hi in self.human_input:
                        for ro in self.robot_output:
                            print ('{0} :::::: {1}'.format(hi, ro))
                            self.txt_input = '{0}\n{1}'.format(self.txt_input, hi)
                            self.txt_output = '{0}\n{1}'.format(self.txt_output, ro)
                    self.human_input = []
                    self.robot_output = []
                continue
            if data[0] == '#':
                continue
            if data[:2] == 'H:':
                #print ("Human")
                data = data[2:]
                if data:
                    #print (data)
                    self.reduce_result = []
                    self.reduce_msg(data)
                    self.human_input += self.reduce_result
                prev = 'human'
            if data[:2] == 'R:':
                self.robot_output.append(data[2:])
                prev = 'robot'
            #print ("'{0}'".format(data))
            
        with open("Input.txt", "w") as text_file:
            text_file.write(self.txt_input)
        with open("Output.txt", "w") as text_file:
            text_file.write(self.txt_output)

compiler = data_compiler()
compiler.compile('rdany_data.txt')
