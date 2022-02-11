#!/bin/sh 
echo "Entrer le nom d'un r�pertoire : " 
read dir 
if [ $# -ne 0 ]; then 
 echo "Erreur : Le script doit �tre appel� avec 1 argument" 1>&2  exit 1 
fi 
if [ ! -d "$dir" ]; then 
 echo "Erreur : \"$dir\" n'est pas un r�pertoire" 1>&2 
 exit 1 
fi 
if [ ! -r "$dir" ]; then 
 echo "Erreur : je ne peux pas lire le r�pertoire \"$dir\"" 1>&2  exit 1 
fi 
