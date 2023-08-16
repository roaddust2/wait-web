(function () {
  try {
    const mainContainer = document.querySelector(".carousel-container");
    if (!mainContainer) return;

    const backgroundContainer = mainContainer.querySelector('.carousel-main');
    const mainImage = mainContainer.querySelector("img");
    const allAsideImg = mainContainer.querySelectorAll(".carousel-aside img");
    const modal = document.querySelector('#carouselModal');
    const modalImg = modal.querySelector('img');
    const modalBg = modal.querySelector('.modal-bg')
    const modalLeft = modal.querySelector('.modal-left')
    const modalRight = modal.querySelector('.modal-right')

    const isPhone = /Android|iPhone/i.test(navigator.userAgent);

    const state = {
      active: 1,
      animating: false,
      // openedModal: () => document.getElementById('carouselModal').getAttribute('aria-hidden'),
    };

    const animation = {
      fadeIn: [{ opacity: 0.3 }, { opacity: 1 }],
      blurTiming: {
        duration: 500,
        iterations: 1,
        easing: 'ease-out'
      },
      animate(imageSrc) {
        state.animating = true;
        backgroundContainer.style.background = (`left top / cover url(${mainImage.src}) no-repeat`);
        !isPhone ? modalBg.style.background = (`left top / cover url(${mainImage.src}) no-repeat`) : '';
        mainImage.src = imageSrc;
        !isPhone ? modalImg.src = imageSrc : '';
        mainImage.animate(this.fadeIn, this.blurTiming)
          .finished.then(r => {
            state.animating = false;
            backgroundContainer.style.background = 'none';
          })
        !isPhone && modalImg.animate(this.fadeIn, this.blurTiming)
          .finished.then(r => {
            state.animating = false;
            modalBg.style.background = 'none';
          })
      }
    }

    if (!isPhone) {
      // All modal events are only added on validation
      backgroundContainer.setAttribute('data-bs-toggle', 'modal')
      backgroundContainer.setAttribute('data-bs-target', '#carouselModal')
      window.removeEventListener("keydown", arrowSliding);
      window.addEventListener("keydown", arrowSliding);
      modalLeft.onclick = () => {
        state.active -= 1;
        if (state.active < 1) state.active = allAsideImg.length;
        arrowControl()
      }
      modalRight.onclick = () => {
        state.active += 1;
        if (state.active > allAsideImg.length) state.active = 1;
        arrowControl()
      }
    }

    // To make an overflow hidden (scroll) for side slides
    setContainerHeight();

    allAsideImg.forEach((image, ind) => {
      if (ind === 0) image.classList.add('image-active');
      image.addEventListener("click", setImage(ind))
    })

    // Handler for side images of a slide
    function setImage(ind) {
      return function () {
        if (state.active === ind + 1 || state.animating) return;
        allAsideImg.forEach((image, index) => {
          if (index === ind) {
            image.classList.add('image-active');
          } else image.classList.remove('image-active');
        })
        state.active = ind + 1;
        animation.animate(this.src)
      };
    }

    function setContainerHeight() {
      const height = mainImage.offsetHeight;
      mainContainer.style.setProperty("--main-height", height);
    }

    // Arrow control handler
    function arrowSliding(e) {
      if (/arrowleft/i.test(e.code) && !state.animating) {
        state.active -= 1;
        if (state.active < 1) state.active = allAsideImg.length;
        arrowControl()
      }
      if (/arrowright/i.test(e.code) && !state.animating) {
        state.active += 1;
        if (state.active > allAsideImg.length) state.active = 1;
        arrowControl()
      }
    }

    // It also works in the modal when you click right / left
    function arrowControl() {
      allAsideImg.forEach((image, index) => {
        if (index === state.active - 1) {
          image.classList.add('image-active');
        } else image.classList.remove('image-active');
      })
      const imageSrc = allAsideImg[state.active - 1].src;
      animation.animate(imageSrc);
    }

  } catch (error) {
    console.warn(error);
  }
})();
