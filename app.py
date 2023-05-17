from flask import Flask, request, jsonify ,render_template
app = Flask(__name__)
import re

@app.route('/')
def description():
    return render_template('index.html')



@app.route('/submit', methods=['POST'])
def handle_submit():
    data = request.json
    print(data)

    keyword = ['False', 'None', 'True', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if','in', 'is', 'lambda', 'nonlocal', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield','import']
    built_in_functions = ['print', 'len', 'input', 'str', 'int', 'float', 'bool', 'range', 'type', 'list', 'set', 'dict', 'max', 'min', 'sum', 'abs', 'round', 'sorted', 'reversed', 'enumerate', 'zip', 'map', 'filter', 'any', 'all', 'dir', 'help', 'id', 'super', 'issubclass', 'isinstance', 'callable', 'eval', 'exec', 'open', 'close', 'os.getcwd', 'os.listdir', 'os.path.exists', 'sys.argv']
    operators = ['+', '-', '', '/', '%', '==', '!=', '>', '<', '>=', '<=', '&', '|', '^', '~', '>>', '<<', '=', '+=', '-=', '=']
    specialsymbol = ['and', 'or', 'not']
    separator = [',', ':', ';', '\n', '\t', '{', '}', '(', ')', '[', ']']
    
    keyword_output =[]
    operators_output=[]
    specialsymbol_output=[]
    built_in_functions_output=[]
    separator_output=[]
    header_line_output=[]
    numerals_output=[]
    identifier_output=[]
    
    contents =data
    splitCode = contents.split() 
    length = len(splitCode)     
    for i in range(0,length):
        if splitCode[i] in keyword :
            print("Keyword -->",splitCode[i])
            keyword_output.append(splitCode[i])
            
        if splitCode[i] in operators:
            print("Operators --> ",splitCode[i])
            operators_output.append(splitCode[i])
            continue
        if splitCode[i] in specialsymbol:
            print("Special Operator -->",splitCode[i])
            specialsymbol_output.append(splitCode[i])
            continue
        if splitCode[i] in built_in_functions:
            print("Built_in Function -->",splitCode[i])
            built_in_functions_output.append(splitCode[i])
            continue
        if splitCode[i] in separator:
            print("Separator -->",splitCode[i])
            separator_output.append(splitCode[i])
            continue
        if re.match(r'(import*).*', splitCode[i]):
            print ("Header File -->", splitCode[i+1])
            header_line_output.append(splitCode[i+1])
            i+=1
            continue
        if re.match(r'^[-+]?[0-9]+$',splitCode[i]):
            print("Numerals --> ",splitCode[i])
            numerals_output.append(splitCode[i])
            continue
        if re.match(r"^[^\d\W]\w*\Z", splitCode[i]):
            print("Identifier --> ",splitCode[i])
            identifier_output.append(splitCode[i])
      
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
    
    print(operators_output)
    return jsonify({'keyword_output': keyword_output ,'operators_output':operators_output ,'specialsymbol_output': specialsymbol_output ,'built_in_functions_output': built_in_functions_output ,'separator_output': separator_output ,'header_line_output':header_line_output ,'numerals_output': numerals_output ,'identifier_output':identifier_output})
  

if __name__ == '__main__':
    app.run(debug=True)












