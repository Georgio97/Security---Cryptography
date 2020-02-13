##
## EPITECH PROJECT, 2019
## Makefile
## File description:
## Gautier PLANCQ
##

NAME	=	challenge

all:		$(NAME)

$(NAME):
		cp ./ch01/challenge01.py ./challenge01
		cp ./ch02/challenge02.py ./challenge02
		cp ./ch03/challenge03.py ./challenge03
		cp ./ch05/challenge05.py ./challenge05

clean:
		rm -f challenge01
		rm -f challenge02
		rm -f challenge03
		rm -f challenge05

fclean:		clean

re:		fclean all