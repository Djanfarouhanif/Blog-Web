//==================Clik Event============
const resp = document.querySelector('.resp');
const responseBtn = document.querySelector('.response-btn');
const btn = document.querySelector('.btn');
const form = document.querySelector('.form');
const annuler = document.querySelector('.annul-container');
console.log(resp);


responseBtn.addEventListener('click', ()=>{
    console.log('btn');
    resp.classList.toggle('response-visible');
    btn.classList.toggle('response-visible');
    form.classList.toggle('form-btn');
    annuler.classList.toggle('response-visible')

});






