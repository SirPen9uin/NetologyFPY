const request = new XMLHttpRequest()
request.addEventListener('readystatechange', () =>{
   if (request.readyState === request.DONE){
       let data = JSON.parse(request.responseText)
       const pollTitle = document.getElementById('poll__title')
       pollTitle.textContent = data.data.title
       const btns = document.getElementById('poll__answers')
       for (let i of data.data.answers){
          btns.innerHTML +=
            `<button class="poll__answer">
              ${i}
             </button>`
        }
       const btn = document.querySelectorAll('.poll__answer')
       for (let k of btn){
            k.onclick = () => {
                alert('Спасибо Ваш голос учтён')
            }
        }
    }
})
request.open('GET', 'https://students.netoservices.ru/nestjs-backend/poll')
request.send()