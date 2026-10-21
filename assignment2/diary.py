import traceback
new_entry =''
try:
    with open('./diary.txt', 'a') as file:
        new_entry = input("What happened today?: ")
        file.write(new_entry + "\n")
        while(new_entry.lower() != "done for now"):
                new_entry = input("What else?: ") 
                file.write(new_entry + "\n")
except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")