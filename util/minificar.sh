#!/bin/sh

#cd cualbondi's git root
java -jar util/closure-compiler.jar --js apps/core/static/js/functions-2.0.js --js_output_file /tmp/functions-2.0.js
mv /tmp/functions-2.0.js ../static/js/functions-2.0.js

java -jar util/closure-compiler.jar --js apps/core/static/js/vr-1.0.js --js_output_file /tmp/vr-1.0.js
mv /tmp/vr-1.0.js ../static/js/vr-1.0.js
