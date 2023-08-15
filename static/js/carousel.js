(function () {
  try {
    const mainContainer = document.querySelector(".carousel-container");
    if (!mainContainer) return;
    const backgroundContainer = mainContainer.querySelector('.carousel-main');
    const mainImage = mainContainer.querySelector("img");
    const allAsideImg = mainContainer.querySelectorAll(".carousel-aside img");
    const modalImg = document.querySelector('#carouselModal img');

    const state = {
      active: 1,
      animating: false,
      openedModal: () => document.getElementById('carouselModal').getAttribute('aria-hidden'),
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
        mainImage.src = imageSrc;
        modalImg.src = imageSrc;
        mainImage.animate(this.fadeIn, this.blurTiming)
        .finished.then(r => {
          state.animating = false;
          backgroundContainer.style.background = 'none';
        })
      }
    }

    if (!/Android|iPhone/i.test(navigator.userAgent)) {
      backgroundContainer.setAttribute('data-bs-toggle', 'modal')
      backgroundContainer.setAttribute('data-bs-target', '#carouselModal')
    }

    setContainerHeight();

    allAsideImg.forEach((image, ind) => {
      if (ind === 0) image.classList.add('image-active');
      image.addEventListener("click", setImage(ind))
    })

    window.removeEventListener("keydown", arrowSliding);
    window.addEventListener("keydown", arrowSliding);


    
    function setImage(ind) {
      return function() {
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

    function arrowSliding(e) {
      const modal = state.openedModal()
      if (/arrowleft/i.test(e.code) && !state.animating && modal) {
        state.active -= 1;
        if (state.active < 1) state.active = allAsideImg.length;
        arrowControl()  
      }
      if (/arrowright/i.test(e.code) && !state.animating && modal) {
        state.active += 1;
        if (state.active > allAsideImg.length) state.active = 1;
        arrowControl()
      }

      function arrowControl() {
        allAsideImg.forEach((image, index) => {
          if (index === state.active - 1) {
            image.classList.add('image-active');
          } else image.classList.remove('image-active');
        })
        const imageSrc = allAsideImg[state.active - 1].src;
        animation.animate(imageSrc);
      }
    }

  } catch (error) {
    console.warn(error);
  }
})();
