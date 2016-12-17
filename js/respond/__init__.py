from fanstatic import Library, Resource

library = Library('respond.js', 'resources')

# Define the resources in the library like this.
# For options and examples, see the fanstatic documentation.
# resource1 = Resource(library, 'style.css')

respond = Resource(library, 'respond.src.js', minified='respond.min.js')

respond_matchmedia = Resource(library, 'respond.matchmedia.addListener.src.js', minified='respond.matchmedia.addListener.min.js')
