import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from userprofile.models import Peer,Clubs

# Create a GraphQL type for the Peer model
class PeerType(DjangoObjectType):
    class Meta:
        model = Peer

# Create a GraphQL type for the movie model
class ClubsType(DjangoObjectType):
    class Meta:
        model = Clubs


class Query(ObjectType):
    peer = graphene.Field(PeerType, id=graphene.Int())
    club = graphene.Field(ClubsType, id=graphene.Int())
    peers = graphene.List(PeerType)
    clubs= graphene.List(ClubsType)
    

    def resolve_peer(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Peer.objects.get(pk=id)

        return None

    def resolve_clubs(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Clubs.objects.get(pk=id)

        return None

    def resolve_peers(self, info, **kwargs):
        return Peer.objects.all()

    def resolve_clubs(self, info, **kwargs):
        return Clubs.objects.all()

class PeerInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()

class ClubsInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    peers = graphene.List(PeerInput)
    
    


# Create mutations for actors
class CreatePeer(graphene.Mutation):
    class Arguments:
        input = PeerInput(required=True)

    ok = graphene.Boolean()
    peer = graphene.Field(PeerType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        peer_instance = Peer(name=input.name)
        peer_instance.save()
        return CreatePeer(ok=ok, peer=peer_instance)

class UpdatePeer(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = PeerInput(required=True)

    ok = graphene.Boolean()
    peer = graphene.Field(PeerType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        peer_instance = Peer.objects.get(pk=id)
        if peer_instance:
            ok = True
            peer_instance.name = input.name
            peer_instance.save()
            return UpdatePeer(ok=ok, peer=peer_instance)
        return UpdatePeer(ok=ok, peer=None)


class CreateClubs(graphene.Mutation):
    class Arguments:
        input = ClubsInput(required=True)

    ok = graphene.Boolean()
    clubs = graphene.Field(ClubsType)
    Peer=[]

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        peers = []
        for peer_input in input.peers:
          peer = Peer.objects.get(pk=peer_input.id)
          if peer is None:
            return CreateClubs(ok=False, clubs=None)
          peers.append(peer)
        clubs_instance = Clubs(
          title=input.title,
          
          )
        clubs_instance.save()
        clubs_instance.peers.set(peers)
        return CreateClubs(ok=ok, clubs=clubs_instance)


class UpdateClubs(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = ClubsInput(required=True)

    ok = graphene.Boolean()
    clubs = graphene.Field(ClubsType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        clubs_instance = Clubs.objects.get(pk=id)
        if clubs_instance:
            ok = True
            peers = []
            for peer_input in input.peers:
              peer = Peer.objects.get(pk=peer_input.id)
              if peer is None:
                return UpdateClubs(ok=False, clubs=None)
              peers.append(peer)
            clubs_instance.title=input.title
            
            clubs_instance.save()
            clubs_instance.peers.set(peers)
            return UpdateClubs(ok=ok, clubs=clubs_instance)
        return UpdateClubs(ok=ok, cluns=None)


class Mutation(graphene.ObjectType):
    create_peer = CreatePeer.Field()
    update_peer = UpdatePeer.Field()
    create_clubs = CreateClubs.Field()
    update_clubs = UpdateClubs.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

