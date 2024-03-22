# Utilisez une image Nginx de base
FROM nginx:alpine

# Copiez vos fichiers HTML, CSS et JavaScript dans le répertoire de travail de Nginx
COPY ./ /usr/share/nginx/html

# Démarrez Nginx lors du lancement du conteneur
CMD ["nginx", "-g", "daemon off;"]
