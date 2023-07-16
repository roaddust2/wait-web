# Contributing

1. Choose an issue ar create one (https://github.com/roaddust2/wait-web/issues)
2. Fork the repository
3. Read installation instructions [here](INSTALLATION.md)
4. Clone the repo and install the app
5. Create new branch for a feature **git checkout -b new-feature**
6. Make changes
7. Write tests if possible
8. Run linter **make lint**, we use flake8 standarts
9. Run tests **make test**
10. Add and commit changes **git commit -am 'Added some feature'**
11. Push changes **git push origin new-feature**
12. Create new Pull Request on GitHub
13. Don't forget to add GitHub Action vars to your fork, otherwise PR check will fail:  
    secret **DJANGO_SECRET_KEY** with something like secret_key123  
    variable **DJANGO_DEBUG** with **True**  
    variable **DJANGO_ALLOWED_HOSTS** with **127.0.0.1,localhost,0.0.0.0**  
15. Wait, until PR is reviewed
16. You are awesome :)
