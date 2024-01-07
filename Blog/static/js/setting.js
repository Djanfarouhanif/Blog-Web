//==================Upload Profile========================
const profile = document.querySelector('.profile');
const upload = document.querySelector('.upload-profile');
const annuler = document.querySelector('.annul');

console.log(upload);

profile.addEventListener('click', ()=>{
    console.log(upload)
    upload.classList.toggle('up');
    
});

