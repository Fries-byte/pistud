<p align="center">
  
  ![Banner](https://github.com/user-attachments/assets/2912f1f3-4c54-4d49-86a3-acf5b147a244)
</p>
<h4 align="center">
  
  [Website](https://pust-lang.github.io/web/)
  
</h4>
<hr>
<p align="center">
  <b>Pust</b> – A Rust-inspired programming language  
  This program is in pre-release. The full code is still under development.
</p>


<br>

## What is Pust?

Pust is a new low-level programming language inspired by Rust.  
Our goal is to offer powerful, safe, and concurrent programming capabilities with an easier learning curve.  
Think **Rust**, but with **Pust** simplicity and elegance!

---

## Features (Work in Progress)

- **Easy to use**: Pust is easy to use, like, pln, iln, fn, wo, if_stmt and cv!
- **Usefull**: Pust is written it so that its easy to code for bigginers, it might also be usefull
- **Software**: Currently this is not fully added yet, but in the furture this language

---
## How to program
- **Mainspace**: Mainspace is where you can code without using the p. , like this: p.fn("main", ['pln("my coding space")']) <br> <br>
- **Print**: To print in Pust in use pln("") or p.pln("") if it isnt in mainspace <br> <br>
- **Input**: If you want user input, use iln("") or add the p. if not in mainspace, and this is how to give an input a variable to add in an if statement or print: cv("variable", "put anything you want, it wont be used") = iln("Hello: "), and it'll take the user input and save it into the variable <br> <br>
- **if_stmt**: to use an if statement, use ```p.if_stmt("variable", "value", ['pln("Hello!")'], ['pln("Bye!")'])```, this part "variable", "value", you could say if variable is value then pln("Hello!") else pln("Bye!"), else is optinal. ```p.if_stmt(if > "variable", is > "value", then > ['pln("Hello!")'], else > ['pln("Bye!")'])``` <br> <br>
- **Functions**: Currently sometimes functions does not work in Mainspace, so you have to use with p. : p.fn("MyFunc", ['code']) <br> <br>
- **Variables**: Variables, to create a variable, use cv("VariableName", "Value"), to print or Input a variable, use pln("VariableName") and input, if its outside of Mainspace use variable = p.iln("Type Hello: ") like in basic python. <br> <br>
- **Copy Paste**: mainspace ``` p.fn("main", [' code here ']) ```, print ``` p.pln('Hello World!') ```, input ``` p.iln('Type somthing: ') ```, variables ``` p.cv('VName', 'Vvalue') ```, if statement ```p.if_stmt("variable", "value", ['pln("Hello!")'], ['pln("Bye!")'])```, web open ```p.wo('url')``` <br> <br>


## Getting Started
Download [python](https://python.org) before crossing the line! <br>
🚧 The language is in its early stages. 🚧  <br>
However, if you're curious and would like to experiment: <br>

1. Clone the repository: <br>  
   ```bash
   git clone https://github.com/Pust-Lang/Pust
   ```
2. Run the files <br>
   Run and open the file named 'main.py', you'll be seeing "p.fn("main", [""]). In between the [""] is where you code, you may also not use Mainspace, but you need to add p. , like this: p.pln("Hello World!") <br>
   To learn Pust, go in our website and click on "cource" (still in development!) <br>

Have fun!
