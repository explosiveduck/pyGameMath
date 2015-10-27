import math
import six

# Spherical Harmonics Vertex
class SPHVertex(object):

    def __init__(self, position, normal):
        # Value of a vertex
        self.position = position

        # calc normal from position self.normal
        self.normal = normal
        # or can be specified from outside of function (from file parser)

        # Arrays; length: undefined
        self.unshadowedCoeffs = None
        self.shadowedCoeffs = None


# Spherical Harmonics Object
class SPHObject(object):

    def __init__(self, indices, vertices):
        # Arrays
        self.vertices = vertices
        self.indices = indices
        # Booleans
        # CollisionResponse = False # wasnt being used so commented it out


# Generate Coefficients
# objects is an array that holds the objects in the scene
def GenereateCoeffs(numSamples, numBands, samples, objects):

    numFunctions = numBands * numBands
    numObjects = len(objects)

    # Create space for the SH coefficients in each vertex
    for i in six.range(numObjects):

        currentObject = objects[i]

        numVertices = len(currentObject.vertices)

        for j in six.range(numVertices):

            currentVertex = currentObject.vertices[j]

            # Create new unshadowedCoeffs array
            # Create new shadowedCoeffs array

    for i in six.range(numObjects):

        currentObject = object[i]

        numVertices = len(currentObject.vertices)

        for j in six.range(numVertices):

            currentVertex = currentObject.vertices[j]

            for k in six.range(numFunctions):
                currentVertex.unshadowedCoeffs[k] = 0.0
                currentVertex.shadowedCoeffs[k] = 0.0

            for k in six.range(numSamples):
                dotProduct = samples[k].dir.dot(currentVertex.normal)

                # Clamp to [0,1]
                if dotProduct > 0.0:

                    # Ray structure

                    # Collision check

                    for l in six.range(numFunctions):
                        contribution = dotProduct * samples[k].values[l]
                        currentVertex.unshadowedCoeffs[l] += contribution
                        #if not rayBlocked:
                        #    currentVertex.shadowedCoeffs[l] += contribution

        # Rescale the coefficients
        for k in six.range(numFunctions):
            currentVertex.unshadowedCoeffs[k] *= 4 * math.pi / numSamples
            currentVertex.shadowedCoeffs[k] += 4 * math.pi / numSamples
