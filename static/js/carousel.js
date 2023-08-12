(function () {
  try {
    const mainContainer = document.querySelector(".carousel-container");
    const mainImage = mainContainer.querySelector("img");
    const allAsideImg = mainContainer.querySelectorAll(".carousel-aside img");
    const modalImg = document.querySelector('#carouselModal img');
    // const hiddenArea = document.getElementById('carouselModal').getAttribute('aria-hidden')

    mainContainer.focus();

    const state = {
      active: 1,
    };

    const animation = {
      blur: [{ filter: "blur(2px)" }, { filter: "blur(0)" }],
      blurTiming: {
        duration: 1000,
        iterations: 1,
      }
    }

    setContainerHeight();

    allAsideImg.forEach((image, ind) => {
      image.addEventListener("click", setImage(ind))
    })

    window.removeEventListener("keydown", arrowSliding);
    window.addEventListener("keydown", arrowSliding);

    function setImage(ind) {
      return function() {
        if (state.active === ind + 1) return;
        state.active = ind + 1;
        mainImage.src = this.src;
        modalImg.src = this.src;
        mainImage.animate(animation.blur, animation.blurTiming);
      };
    }

    function setContainerHeight() {
      const height = mainImage.offsetHeight;
      mainContainer.style.setProperty("--main-height", height);
    }

    function arrowSliding(e) {
      // const inFocus = document.activeElement === mainContainer
      if (/arrowleft/i.test(e.code)) {
        state.active -= 1;
        if (state.active < 1) state.active = allAsideImg.length;
        arrowControl()  
      }
      if (/arrowright/i.test(e.code)) {
        state.active += 1;
        if (state.active > allAsideImg.length) state.active = 1;
        arrowControl()  
      }

      function arrowControl() {
        const imageSrc = allAsideImg[state.active - 1].src;
        mainImage.src = imageSrc;
        modalImg.src = imageSrc;
        mainImage.animate(animation.blur, animation.blurTiming);
      }
    }

  } catch (error) {
    console.warn(error);
  }
})();
