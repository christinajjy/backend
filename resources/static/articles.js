const app1 = document.getElementById('Articles');
const container1 = document.createElement('div');
container1.setAttribute('class', 'container');
app1.appendChild(container1);

var request1 = new XMLHttpRequest();

request1.open('GET', 'https://retoolapi.dev/f5Fqw2/articles', true);
request1.onload = function () {
    var data = JSON.parse(this.response);

    const articles = data;
    if (request1.status >= 100 && request1.status < 400) {
        const max = 9;
        articles.slice(0, max).forEach((article) => {
            const card = document.createElement('div');
            card.setAttribute('class', 'card');

            const a = document.createElement('a');
            a.setAttribute('href', article.url); // Assuming there's a 'url' property in each article
            a.setAttribute('target', '_blank'); // Open the link in a new tab

            const h1 = document.createElement('h1');
            h1.setAttribute('id', 'news-title');
            h1.textContent = `${article.title.slice(0, 70)}...`;

            const img = document.createElement('img');
            img.src = article.image;
            img.setAttribute('class', 'icon');

            container1.appendChild(a);
            a.appendChild(card);
            card.appendChild(img);
            card.appendChild(h1);
        });
    } else {
        const errorMsg = document.createElement('p');
        errorMsg.textContent = `Not Found`;
        app1.appendChild(errorMsg);
        console.error(error);
    }
};

request1.send();
