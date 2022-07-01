from transliterate import translit
from num2words import num2words


text = f"""Ladies and gentlemen, I'm {num2words(78, to='cardinal')} years old and I finally got {num2words(15, to='cardinal')} minutes of fame once in a lifetime and I guess that this is mine. People have also told me to make these next few minutes escruciatingly embarrassing and to take vengeance of my enemies. Neither will happen. 

More than {num2words(3, to='cardinal')} years ago I moved to Novo-Novsk, but worked on new Magnetic Storage for last {num2words(40, to='cardinal')}. When I was {num2words(8, to='cardinal')}..."""
print(translit(text, 'ru'))
