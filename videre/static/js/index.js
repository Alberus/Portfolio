
let projects = [
    {
        name: 'Portfolio',
        desc: 'Construído em Python (Flask) banco de dados integrado e com arquitetura que evita circular imports utilizando formato de factory e Blueprints.',
        image: 'static/img/Slider 1.png'
    },
    {
        name: 'Historiaflix',
        desc: 'Um clone da Netflix para mídias diversas de História.',
        image: 'static/img/Slider 2.png'
    },
    {
        name: 'Resgate Game',
        desc: 'Um jogo 2D simples com Javascript.',
        image: 'static/img/Slider 3.png'
    },
    {
        name: 'CRUD',
        desc: 'Create, read, update e delete registros de estudantes em banco de dados SQLite e ORM SQLAlchemy.',
        image: 'static/img/Slider 4.png'
    },
    {
        name: '',
        desc: '',
        image: ''
    },
]




const carousel = document.querySelector('.carousel');

let sliders = [];

let slideIndex = 0;

const createSlide = () => {
    if(slideIndex>=projects.lenght){
        slideIndex = 0;
    }
    //creating DOM element
    let slide = document.createElement('div');
    let imgElement = document.createElement('img');
    let content = document.createElement('div');
    let h1 = document.createElement('h1');
    let p = document.createElement('p');

    //attaching all elements
    imgElement.appendChild(document.createTextNode(''));
    h1.appendChild(document.createTextNode(projects[slideIndex].name));
    p.appendChild(document.createTextNode(projects[slideIndex].desc));
    content.appendChild(h1);
    content.appendChild(p);
    slide.appendChild(content);
    slide.appendChild(imgElement);
    carousel.appendChild(slide);

    //setting up image
    imgElement.src = projects[slideIndex].image;
    slideIndex ++;

    //setting elements classname
    slide.className = 'slider';
    content.className = 'slide-content';
    h1.className = 'project-title';
    p.className = 'project-desc';

    sliders.push(slide);

    //adding sliding effect

    if(sliders.length){
        sliders[0].style.marginLeft = `calc(-${100 * (sliders.length - 2)}% - ${30 * (sliders.length - 2)}px)`;
    }
}

for(let i = 0; i < 2; i++){
    createSlide();
}

setInterval(() => {
  createSlide();  
}, 5000);


//projects video cards

const videoCards = [...document.querySelectorAll('.video-card')];

videoCards.forEach(item => {
    item.addEventListener('mouseover', () => {
        let video = item.children[1];
        video.play();
    })
    item.addEventListener('mouseleave', () => {
        let video = item.children[1];
        video.pause();
    })
})

//create sliders

let cardContainers = [...document.querySelectorAll('.card-container')];
let preBtns = [...document.querySelectorAll('.pre-btn')];
let nxtBtns = [...document.querySelectorAll('.nxt-btn')];

cardContainers.forEach((item, i) => {
    let containerDimensions = item.getBoundingClientRect();
    let containerWidth = containerDimensions.width;

    nxtBtns[i].addEventListener('click', () => {
        item.scrollLeft += containerWidth - 200;
    })

    preBtns[i].addEventListener('click', () => {
        item.scrollLeft -= containerWidth + 200;
    })
})


