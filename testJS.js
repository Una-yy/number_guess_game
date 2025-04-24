let message = "Hello!";
const PI = 3.14159;
message = "World!"; // 再代入可能
// PI = 3.14; // エラー！再代入不可
console.log(message); //ブラウザのコンソールに""World!"と表示
console.log(PI); // ブラウザのコンソールに3.14159と表示

function greet(name){
  console.log("こんにちは、" + name + "さん！");
}

greet("JavaScript"); //こんにちは、JavaScriptさん！と表示

messageElement.textContent = "新しいメッセージ！"
messageElement.style.color = "red";
buttonElement.style.backgroundColor = "lightblue";
