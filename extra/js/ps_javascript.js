// Piargs package reader for Pistud
// for JavaScript
    function loadPiPackage([]){
        class PustInterpreter {
            constructor() {
                this.variables = {};
                this.functions = {};
                this.windows = {};
                this.customKeys = {};
            }
    
            newkey(key, code) {
                this.customKeys[key] = code;
            }
    
            py(execJS) {
                eval(execJS);
            }
    
            bash(command) {
                console.warn("Bash execution is not available in JavaScript.");
            }
    
            load(url) {
                fetch(url)
                    .then(response => response.text())
                    .then(script => eval(script))
                    .catch(error => console.error("Error loading script:", error));
            }
    
            cw(wtitle, geo) {
                let windowDiv = document.createElement("div");
                windowDiv.style.position = "absolute";
                windowDiv.style.width = geo.split("x")[0] + "px";
                windowDiv.style.height = geo.split("x")[1] + "px";
                windowDiv.style.border = "1px solid black";
                windowDiv.style.background = "white";
                windowDiv.style.padding = "10px";
                windowDiv.innerHTML = `<h3>${wtitle}</h3>`;
                document.body.appendChild(windowDiv);
                this.windows[wtitle] = windowDiv;
                return windowDiv;
            }
    
            ct(windowname, geo, text) {
                if (this.windows[windowname]) {
                    let label = document.createElement("p");
                    label.innerText = text;
                    this.windows[windowname].appendChild(label);
                } else {
                    console.error(`Error: Window '${windowname}' not found.`);
                }
            }
    
            wl(wname) {
                console.log(`Window '${wname}' is now active.`);
            }
    
            let(varName, val) {
                this.variables[varName] = val;
            }
    
            wo(url) {
                window.open(url, "_blank");
            }
    
            mb(type, title, message) {
                if (type === "info") alert(`${title}: ${message}`);
                else if (type === "warning") console.warn(`${title}: ${message}`);
                else if (type === "error") console.error(`${title}: ${message}`);
            }
    
            pln(text, ...args) {
                args.forEach((arg, i) => {
                    text = text.replace(`{${i}}`, arg);
                });
                for (let key in this.variables) {
                    text = text.replace(`{${key}}`, this.variables[key]);
                }
                console.log(text);
            }
    
            iln(promptText) {
                return prompt(promptText);
            }
    
            if_stmt(varName, value, codeIf, codeElse = null) {
                if (this.variables[varName] === value) {
                    eval(codeIf);
                } else if (codeElse) {
                    eval(codeElse);
                }
            }
    
            cb(windowname, geo, size, name) {
                if (this.windows[windowname]) {
                    let button = document.createElement("button");
                    button.innerText = name;
                    button.style.width = size.split(",")[0] + "px";
                    button.style.height = size.split(",")[1] + "px";
                    this.windows[windowname].appendChild(button);
                    this.windows[`${windowname}_${name}_button`] = button;
                } else {
                    console.error(`Error: Window '${windowname}' not found.`);
                }
            }
    
            bc(name, code) {
                for (let key in this.windows) {
                    if (key.endsWith(`_${name}_button`)) {
                        this.windows[key].onclick = () => eval(code);
                        console.log(`Click event bound to button '${name}'.`);
                        return;
                    }
                }
                console.error(`Error: Button '${name}' not found.`);
            }
    
            fn(name, code) {
                this.functions[name] = code;
            }
    
            loop(code, n) {
                if (n === 0) {
                    while (true) {
                        eval(code);
                    }
                } else {
                    for (let i = 0; i < n; i++) {
                        eval(code);
                    }
                }
            }
    
            math(expression) {
                try {
                    for (let key in this.variables) {
                        expression = expression.replace(`{${key}}`, this.variables[key]);
                    }
                    return eval(expression);
                } catch (error) {
                    console.error("Error evaluating math expression:", error);
                    return null;
                }
            }
    
            catch(code, errorHandler) {
                try {
                    eval(code);
                } catch (error) {
                    let errorMsg = error.message;
                    let formattedHandler = errorHandler.replace("{!error!}", "Error Found").replace("{!reason!}", errorMsg);
                    eval(formattedHandler);
                }
            }
        }
    
        const piargs = new PustInterpreter();
    }
