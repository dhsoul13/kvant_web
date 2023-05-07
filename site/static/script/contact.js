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

const visibleSuccess = (body) => {
  try {
    const keyInfoByScreen = ['html_url', 'login', 'public_repos', 'avatar_url'];

    const visibleContent = Object.fromEntries(
      keyInfoByScreen.map((el) => [el, body[el]])
    );

    return `<div class="contact">
        <div class="contact__main-info">
          <h2 class="contact__title">Основная информация</h2>
          <ul class="contact__list">
            <li class="contact__list-item">
              <span class="contact__list-key">Имя и фамилия:</span>
              <span class="contact__list-value">Даниил Мухреев</span>
            </li>
            <li class="contact__list-item">
              <span class="contact__list-key">Ссылка на git:</span>
              <span class="contact__list-value"><a href="${visibleContent['html_url']}">клик</a></span>
            </li>
            <li>
              <span class="contact__list-key">Логин:</span>
              <span class="contact__list-value">${visibleContent['login']}</span>
            </li>
            <li>
              <span class="contact__list-key">Колличество репозиториев:</span>
              <span class="contact__list-value">${visibleContent['public_repos']}</span>
            </li>
            <li>
              <span class="contact__list-key">Телеграм</span>
              <span class="contact__list-value"><a href="https://t.me/dhsoul13">https://t.me/dhsoul13</a></span>
            </li>
            
          </ul>
        </div>
        <div class="contact__main-img">
          <img src=${visibleContent['avatar_url']}>
        </div>
    </div>`;
  } catch (error) {
    return visibleError();
  }
};

const requestGitHub = async (domElem) => {
  try {
    domElem.innerHTML = visiblePreloader();

    const response = await fetch('https://api.github.com/users/dhsoul13');
    const body = await response.json();

    domElem.innerHTML = visibleSuccess(body);
  } catch (err) {
    console.log(err);
    domElem.innerHTML = visibleError();
  }
};

function ready() {
  const app = document.querySelector('.app');
  requestGitHub(app);
}

document.addEventListener('DOMContentLoaded', ready);
