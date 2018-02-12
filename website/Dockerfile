# You should always specify a full version here to ensure all of your developers
# are running the same version of Node.
FROM node:9.5.0

ARG http_proxy
ARG https_proxy
ARG no_proxy

RUN export http_proxy=$http_proxy \
  && export https_proxy=$https_proxy \
  && export no_proxy=$no_proxy

# set working directory
COPY ./ .

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

EXPOSE 3000

# install and cache app dependencies
RUN npm install --silent \
&& npm install react-scripts@1.1.0 -g --silent

# start app
CMD ["npm", "start"]
