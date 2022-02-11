#!/bin/sh 
echo "Entrer le nom d'un répertoire : " 
read dir 
if [ $# -ne 0 ]; then 
 echo "Erreur : Le script doit être appelé avec 1 argument" 1>&2  exit 1 
fi 
if [ ! -d "$dir" ]; then 
 echo "Erreur : \"$dir\" n'est pas un répertoire" 1>&2 
 exit 1 
fi 
if [ ! -r "$dir" ]; then 
 echo "Erreur : je ne peux pas lire le répertoire \"$dir\"" 1>&2  exit 1 
fi 
