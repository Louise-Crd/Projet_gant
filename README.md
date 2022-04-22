# Projet_gant

J'ai ajouté 2 versions différentes pour faire la convertion text-to-file:
- la 1ère grâce à la librairie pyttsx3 (sans création de fichier) --> voir text_to_speech_V1
- la 2nde grâce à la librairie gTTs (enregistre l'audio converti dans un fichier mp3) --> voir text_to_speech_V2

Question:
Est-il vraiment nécessaire de créer un fichier pour chaque signe au préalable (ex: chaque lettre de l'alphabet) (cad V2), ou peut-on juste faire en sorte que lorsqu'un signe est effectué et reconnu, le signe en question est automatiquement mis en input (cad V1) ?

Exemple cas V1:
- on effectue la lettre A en LSF
- l'algo de Machine Learning reconnaît la lettre A
- lors de la classification, on donne le nom de la lettre à la classe à laquelle elle appartient
- le code met automatiquement dans le .say "A" qui est donc le signe effectué et le nom de la classe 
--> text_speech.say("A")

Cela permettrait de gagner de la place en évitant de devoir créer des fichier pour chacun des différents audios.

