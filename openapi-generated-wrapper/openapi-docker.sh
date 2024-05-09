docker run --rm -v "$PWD:/local" openapitools/openapi-generator-cli generate \
                                                                             -i https://dracor.org/api/v1/openapi.yaml \
                                                                             -g python \
                                                                             -o /local/auto-generated
