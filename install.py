a
    ���`�  �                   @   s   d dl Z ee �d�� dS )�    Ns�  �                   @   sb   d dl Z ed� ed� e �d� e �d� ed� ze �d� W n eyT   Y n0 ed� dS )	�    Nz[!] Running configuration z'[!] Please don't interrupt this processzpython -m pip install cython z"cythonize -i lib/* /dev/null 2>&1 z"


[!] removing files C extensionsz
rm lib/*.cz[!] Compiled done)�os�print�system�	Exception� r   r   �dg�<module>   s   

)�marshal�exec�loads� r   r   �
install.py�<module>   s   