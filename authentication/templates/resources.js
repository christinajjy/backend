const app = document.getElementById('News')
const container = document.createElement('div')
container.setAttribute('class','container')
app.appendChild(container)


var request = new XMLHttpRequest()

request.open('GET','https://newsapi.org/v2/everything?q=ransomware&from=2023-11-25&to=2023-12-10&sortBy=popularity&language=en&apiKey=2dc6f19f2dc742d489101777dface6b5',true)
request.onload = function() 
{
var data = JSON.parse(this.response)

const news = data.articles

if(request.status >=200 && request.status < 400)
{
    const max = 12;
data.articles.slice(0,max).forEach((news) => {
    const card = document.createElement('div')
    card.setAttribute('class','card')

    /*const a = document.createElement('a')
    a.href=news.url
    a.textcontent= `${news.title.slice(0,70)}...`*/

    const h1 = document.createElement('h1')
    h1.setAttribute('id','news-title')
    h1.href=news.url
    h1.textContent = `${news.title.slice(0,70)}...`

    const p = document.createElement('p')
    p.setAttribute('id','news-info')
    desc = news.description.slice(0,100)
    p.textContent = `${desc}...`

    const img = document.createElement('img')
    img.src=news.urlToImage
    img.setAttribute('class','icon')


    container.appendChild(card)
    card.appendChild(img)
    card.appendChild(h1)
    card.appendChild(p)
})
}
else{
    const errorMsg = document.createElement('p')
    errorMsg.textContent = `Not Found`
    app.appendChild(errorMsg)
}
}
request.send()
