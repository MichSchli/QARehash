class Graphlet:

    entities = None
    events = None
    entity_inverses = None
    event_inverses = None

    def __init__(self, vertex):
        self.center_vertex = vertex
        self.entities = {}
        self.entity_inverses = {}
        self.events = {}
        self.event_inverses = {}

    def add_entity(self, relation, vertex):
        if not relation in self.entities:
            self.entities[relation] = []

        self.entities[relation].append(vertex)

    def add_entity_inverse(self, relation, vertex):
        if not relation in self.entity_inverses:
            self.entity_inverses[relation] = []

        self.entity_inverses[relation].append(vertex)

    def add_event(self, relation, vertex):
        if not relation in self.events:
            self.events[relation] = []

        self.events[relation].append(vertex)

    def add_event_inverse(self, relation, vertex):
        if not relation in self.event_inverses:
            self.event_inverses[relation] = []

        self.event_inverses[relation].append(vertex)

    def __str__(self):
        return "Centroid: " + str(self.center_vertex)\
               + " | Entities: "+str(self.entities)\
               + " | Events: "+ str(self.events)\
               + " | Entities inverse: "+ str(self.entity_inverses)\
               + " | Events inverse: "+ str(self.event_inverses)