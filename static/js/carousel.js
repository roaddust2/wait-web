document.addEventListener('DOMContentLoaded', async () => {
	try {
		const mainContainer = document.querySelector('.carousel-container');
		if (!mainContainer) return;
		const mainImage = mainContainer.querySelector('img');
		const backgroundContainer = mainContainer.querySelector('.carousel-main');
		const allAsideImg = mainContainer.querySelectorAll('.carousel-aside img');
		const allWbpSrc = mainContainer.querySelectorAll('.carousel-aside source');
		const modal = document.querySelector('#carouselModal');
		const modalImg = modal.querySelector('img');
		const modalBg = modal.querySelector('.modal-bg');
		const modalLeft = modal.querySelector('.modal-left');
		const modalRight = modal.querySelector('.modal-right');

		const isPhone = /Android|iPhone/i.test(navigator.userAgent);

		setContainerHeight();

		const initialState = {
			active: 1,
			prev: 0,
			animating: false
		};

		const webpSupport = await (function() {
			const index = new Promise((resolve) => {
				const image = new Image();
				image.addEventListener('error', () => resolve(false));
				image.addEventListener('load', () => resolve(image.width === 1));
				image.src = 'data:image/webp;base64,UklGRiQAAABXRUJQVlA4IBgAAAAwAQCdASoBAAEAAwA0JaQAA3AA/vuUAAA=';
			}).catch(() => false);
			return index;
		})();

		// To make an overflow hidden (scroll) for side slides
		function setContainerHeight() {
			setTimeout(() => {
				const height = mainImage.offsetHeight;
				mainContainer.style.maxHeight = height + 'px';
				mainContainer.querySelector('.carousel-aside').style.maxHeight = height + 'px';
			}, 300);
		}

		// Handler for side images of a slide
		function setImage(state, images, src, ind) {
			return function() {
				if (state.active === ind + 1 || state.animating) return;
				allAsideImg.forEach((image, index) => {
					if (index === ind) {
						image.classList.add('image-active');
					} else image.classList.remove('image-active');
				});
				state.active = ind + 1;
				const prevImg = images[state.prev][src];
				state.prev = ind;
				const srcset = images[ind][src];
				animation.animate(state, srcset, prevImg);
			};
		}

		const animation = {
			fadeIn: [ { opacity: 0.3 }, { opacity: 1 } ],
			blurTiming: {
				duration: 500,
				iterations: 1,
				easing: 'ease-out'
			},
			animate(state, imageSrc, prevSrc) {
				state.animating = true;
				backgroundContainer.style.background = `left top / cover url(${prevSrc}) no-repeat`;
				!isPhone ? (modalBg.style.background = `left top / cover url(${prevSrc}) no-repeat`) : '';
				mainImage.closest('picture').firstElementChild.srcset = imageSrc;
				!isPhone ? (modalImg.src = imageSrc) : '';
				mainImage.animate(this.fadeIn, this.blurTiming).finished.then((r) => {
					state.animating = false;
					backgroundContainer.style.background = 'none';
				});
				!isPhone &&
					modalImg.animate(this.fadeIn, this.blurTiming).finished.then((r) => {
						state.animating = false;
						modalBg.style.background = 'none';
					});
			}
		};

		// It also works in the modal when you click right / left
		function arrowControl(state, images, src) {
			allAsideImg.forEach((image, index) => {
				if (index === state.active - 1) {
					image.classList.add('image-active');
				} else image.classList.remove('image-active');
			});
			const prevImg = images[state.prev - 1][src];
			const srcset = images[state.active - 1][src];
			animation.animate(state, srcset, prevImg);
		}

		function initialActiveImageAndSetImage(state, images, src) {
			allAsideImg.forEach((image, ind) => {
				if (ind === 0) image.classList.add('image-active');
				image.addEventListener('click', setImage(state, images, src, ind));
			});
		}

    	// Arrow control handler
			function arrowSliding(state, images, src) {
        return function(e) {
          if (/arrowleft/i.test(e.code) && !state.animating) {
            state.active -= 1;
            state.prev = state.active + 1;
            if (state.active < 1) state.active = allAsideImg.length;
            arrowControl(state, images, src);
          }
          if (/arrowright/i.test(e.code) && !state.animating) {
            state.active += 1;
            state.prev = state.active - 1;
            if (state.active > allAsideImg.length) state.active = 1;
            arrowControl(state, images, src);
          }
        }
			}

      // All modal events are only added on validation
      function notMobile(state, images, src) {
        if (!isPhone) {
          backgroundContainer.setAttribute('data-bs-toggle', 'modal');
          backgroundContainer.setAttribute('data-bs-target', '#carouselModal');
          window.addEventListener('keydown', arrowSliding(state, images, src));
          modalLeft.onclick = () => {
            state.active -= 1;
            state.prev = state.active + 1;
            if (state.active < 1) state.active = allAsideImg.length;
            arrowControl(state, images, src);
          };
          modalRight.onclick = () => {
            state.active += 1;
            state.prev = state.active - 1;
            if (state.active > allAsideImg.length) state.active = 1;
            arrowControl(state, images, src);
          };
        }
      }

		if (webpSupport) {
			const state = initialState;
			initialActiveImageAndSetImage(state, allWbpSrc, 'srcset');
      notMobile(state, allWbpSrc, 'srcset');
		} else {
			const state = initialState;
			initialActiveImageAndSetImage(state, allAsideImg, 'src');
      notMobile(state, allAsideImg, 'src');
		}
	} catch (error) {
		console.warn(error);
	}
});
