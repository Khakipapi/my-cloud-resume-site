//JavaScript Code 
const counter = document.querySelector(".counter-number");
async function updateCounter(){
    let response = await fetch("https://zkpgcwuukc45xgjuzll3lm3wqa0xfygf.lambda-url.us-east-1.on.aws/");
    let data =await response.json();
    counter.innerHTML = ` Number of visitors : ${data}`;
}
updateCounter();