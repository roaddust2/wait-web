document.addEventListener('DOMContentLoaded', () => {
	(async function() {
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

			// To make an overflow hidden (scroll) for side slides
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

			function setContainerHeight() {
				setTimeout(() => {
					const height = mainImage.offsetHeight;
					mainContainer.style.maxHeight = height + 'px';
					mainContainer.querySelector('.carousel-aside').style.maxHeight = height + 'px';
				}, 300);
			}

			const animation = {
				fadeIn: [ { opacity: 0.3 }, { opacity: 1 } ],
				blurTiming: {
					duration: 500,
					iterations: 1,
					easing: 'ease-out'
				},
				animate(state, imageSrc, prevSrc, webp) {
					state.animating = true;
					backgroundContainer.style.background = `left top / cover url(${prevSrc}) no-repeat`;
					!isPhone ? (modalBg.style.background = `left top / cover url(${prevSrc}) no-repeat`) : '';
					webp === 'src'
						? (mainImage[webp] = imageSrc)
						: (mainImage.closest('picture').firstElementChild[webp] = imageSrc);
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

			if (webpSupport) {
				const state = initialState;

				if (!isPhone) {
					// All modal events are only added on validation
					backgroundContainer.setAttribute('data-bs-toggle', 'modal');
					backgroundContainer.setAttribute('data-bs-target', '#carouselModal');
					window.removeEventListener('keydown', arrowSliding);
					window.addEventListener('keydown', arrowSliding);
					modalLeft.onclick = () => {
						state.active -= 1;
						state.prev -= 1;
						if (state.active < 1) state.active = allAsideImg.length;
						arrowControl();
					};
					modalRight.onclick = () => {
						state.active += 1;
						state.prev -= 1;
						if (state.active > allAsideImg.length) state.active = 1;
						arrowControl();
					};
				}

				allAsideImg.forEach((image, ind) => {
					if (ind === 0) image.classList.add('image-active');
					image.addEventListener('click', setImage(ind));
				});

				// Handler for side images of a slide
				function setImage(ind) {
					return function() {
						if (state.active === ind + 1 || state.animating) return;
						allAsideImg.forEach((image, index) => {
							if (index === ind) {
								image.classList.add('image-active');
							} else image.classList.remove('image-active');
						});
						state.active = ind + 1;
						const prevImg = allWbpSrc[state.prev].srcset;
						state.prev = ind;
						const srcset = allWbpSrc[ind].srcset;
						animation.animate(state, srcset, prevImg, 'srcset');
					};
				}

				// Arrow control handler
				function arrowSliding(e) {
					if (/arrowleft/i.test(e.code) && !state.animating) {
						state.active -= 1;
						state.prev -= 1;
						if (state.active < 1) {
							state.active = allAsideImg.length;
							state.prev = 0;
						}
						arrowControl('left');
					}
					if (/arrowright/i.test(e.code) && !state.animating) {
						state.active += 1;
						state.prev += 1;
						if (state.active > allAsideImg.length) {
							state.active = 1;
							state.prev = allAsideImg.length - 1;
						}
						arrowControl('right');
					}
				}

				// It also works in the modal when you click right / left
				function arrowControl() {
					allAsideImg.forEach((image, index) => {
						if (index === state.active - 1) {
							image.classList.add('image-active');
						} else image.classList.remove('image-active');
					});
					const prevImg = allWbpSrc[state.prev].srcset;
					const srcset = allWbpSrc[state.active - 1].srcset;
					animation.animate(state, srcset, prevImg, 'srcset');
				}
			} else {
				const mainImage = mainContainer.querySelector('img');
				const allAsideImg = mainContainer.querySelectorAll('.carousel-aside img');

				const state = {
					active: 1,
					animating: false
				};

				if (!isPhone) {
					// All modal events are only added on validation
					backgroundContainer.setAttribute('data-bs-toggle', 'modal');
					backgroundContainer.setAttribute('data-bs-target', '#carouselModal');
					window.removeEventListener('keydown', arrowSliding);
					window.addEventListener('keydown', arrowSliding);
					modalLeft.onclick = () => {
						state.active -= 1;
						if (state.active < 1) state.active = allAsideImg.length;
						arrowControl();
					};
					modalRight.onclick = () => {
						state.active += 1;
						if (state.active > allAsideImg.length) state.active = 1;
						arrowControl();
					};
				}

				allAsideImg.forEach((image, ind) => {
					if (ind === 0) image.classList.add('image-active');
					image.addEventListener('click', setImage(ind));
				});

				// Handler for side images of a slide
				function setImage(ind) {
					return function() {
						if (state.active === ind + 1 || state.animating) return;
						allAsideImg.forEach((image, index) => {
							if (index === ind) {
								image.classList.add('image-active');
							} else image.classList.remove('image-active');
						});
						state.active = ind + 1;
						animation.animate(this.src);
					};
				}

				function setContainerHeight() {
					const height = mainImage.offsetHeight;
					mainContainer.style.setProperty('--main-height', height);
				}

				// Arrow control handler
				function arrowSliding(e) {
					if (/arrowleft/i.test(e.code) && !state.animating) {
						state.active -= 1;
						if (state.active < 1) state.active = allAsideImg.length;
						arrowControl();
					}
					if (/arrowright/i.test(e.code) && !state.animating) {
						state.active += 1;
						if (state.active > allAsideImg.length) state.active = 1;
						arrowControl();
					}
				}

				// It also works in the modal when you click right / left
				function arrowControl() {
					allAsideImg.forEach((image, index) => {
						if (index === state.active - 1) {
							image.classList.add('image-active');
						} else image.classList.remove('image-active');
					});
					const imageSrc = allAsideImg[state.active - 1].src;
					animation.animate(imageSrc);
				}
			}
		} catch (error) {
			console.warn(error);
		}
	})();
});
