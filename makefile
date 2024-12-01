DAY ?= 1
TARGET ?= c

SRC = $(wildcard day$(DAY)/*.$(TARGET))
OBJ = $(SRC:.$(TARGET)=.o)
NAME = day$(DAY)_$(TARGET)

CFLAGS = -Wall -Wextra -Werror

GCC = gcc

all: $(NAME)

ifeq ($(TARGET), c)
$(NAME): $(OBJ)
    $(GCC) $(CFLAGS) -o $(NAME) $(OBJ)
else ifeq ($(TARGET), asm)
$(NAME): $(SRC)
	nasm -f elf32 $(SRC) -o $(OBJ)
	ld -m elf_i386 -o $(NAME) $(OBJ)
else ifeq ($(TARGET), py)
$(NAME): $(SRC)
	cp $(SRC) $(NAME).py
endif

.PHONY: clean
clean:
	rm -f $(OBJ)

.PHONY: fclean
fclean: clean
	rm -f $(NAME)

.PHONY: re
re: fclean all
