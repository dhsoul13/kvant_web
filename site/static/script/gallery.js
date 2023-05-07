const URL_BD = 'https://api.jsonbin.io/v3/b/64573e599d312622a3593855';
const BASE_URL = new window.URL(document.URL).origin;

const visibleImgs = (src) => {
  return `<div class="col s12 m4">
  <div class="card">
  <div class="card-image">
    <img src=${src} alt="изображение" loading="lazy">
    </div>
    </div>
  </div>`;
};

const visiblePreloader = () => {
  return `<div>
        Загрузка
    </div>`;
};

const visibleError = () => {
  return `<div>
    Непредвидмая ошибка, попробуйте перезагрузить страницу
    </div>`;
};

const visibleSuccess = (body, location) => {
  const titleFromButton = body.map((el) => el.type);
  const imgsFromVisible = body.reduce((acc, elem) => {
    if (location === '/gallery') {
      acc.push(elem.imgs);
      return acc;
    }

    if (location === '/gallery/seo') {
      if (elem.type === 'seo') {
        acc.push(elem.imgs);
        return acc;
      }
    }

    if (location === '/gallery/frontend') {
      if (elem.type === 'frontend') {
        acc.push(elem.imgs);
        return acc;
      }
    }

    if (location === '/gallery/backend') {
      if (elem.type === 'backend') {
        acc.push(elem.imgs);
        return acc;
      }
    }

    return acc;
  }, []);

  console.log();

  return `<div>
  ${titleFromButton
    .map(
      (el) =>
        `<button class="waves-effect waves-light btn">
          <a href="${BASE_URL}/gallery/${el}" class="link">${el}</a>
        </button>`
    )
    .join(' ')}

    <div class="row">
      ${imgsFromVisible.map((src) => visibleImgs(src)).join(' ')}
    </div>
</div>`;
};

const requestFromJSONBin = async (domElem, location) => {
  try {
    domElem.innerHTML = visiblePreloader();
    const request = await fetch(URL_BD);
    const { record: body } = await request.json();

    domElem.innerHTML = visibleSuccess(body, location);
  } catch (error) {
    domElem.innerHTML = visibleError();
  }
};

function ready() {
  const app = document.querySelector('.app');
  const location = new window.URL(document.URL).pathname;

  requestFromJSONBin(app, location);
}

document.addEventListener('DOMContentLoaded', ready);
