#!/usr/bin/env python
#Author: Hacker NoDo
import hashlib
from colorama import init, Fore, Back,Style
print(Fore.GREEN+'''****     **          *******
/**/**   /**         /**////**
/**//**  /**  ****** /**    /**  ******
/** //** /** **////**/**    /** **////**
/**  //**/**/**   /**/**    /**/**   /**
/**   //****/**   /**/**    ** /**   /**
/**    //***//****** /*******  //******
//      ///  //////  ///////    //////
''')


print("Hacker NoDo => canal oficial = https://youtube.com/@hackerNoDo\n")

x = str(input("Ingresa contraseña a combertir a md5 :  "))

sha1pass = hashlib.sha1(x.encode('utf-8')).hexdigest()

print(Fore.YELLOW+"Tu Clave Hash SHA1 es ↓↓↓↓\n\n", sha1pass)
print(Fore.YELLOW+"\n\nNOTA:=> COPIALA Y PEGALA COMO UNA CLAVE NORMAL SIN PERDERLA AL SER ASI ES DIFICIL QUE LA HACKEN AL PERDERLA VUELVE A INGRESAR EN EL SCRIP TAL COMO LA PUSISTE Y TE DARA LA MISMA CLAVE SHA1, ESTO ES PARA EVITAR LOS ATAQUES DE FUERZA BRUTA\n\n")
print("GRACIAS POR OCUPAR LA HERRAMIENTA ✓ HACKER NoDo Subcribete ✓")
