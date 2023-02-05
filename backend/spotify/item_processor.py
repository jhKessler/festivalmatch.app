import logging

from database.models import (ArtistRequest, ArtistTrack, SpotifyArtist,
                             SpotifyRequest, SpotifyTrack, TrackRequest)

logger = logging.getLogger(__name__)


class ItemProcessor:

    @staticmethod
    def save_and_return_artist(item: dict) -> SpotifyArtist:
        artist = SpotifyArtist.from_item(item)
        if SpotifyArtist.select().where(SpotifyArtist.id == artist.id).exists():
            logger.debug(f"Artist {artist.name} already exists.")
        else:
            logger.debug(f"Artist {artist.name} does not exist. Saving...")
            artist.save(force_insert=True)
        return artist

    @staticmethod
    def save_and_return_track(item: dict) -> SpotifyTrack:
        track = SpotifyTrack.from_item(item)
        if SpotifyTrack.select().where(SpotifyTrack.id == track.id).exists():
            logger.debug(f"Track {track.name} already exists.")
        else:
            logger.debug(f"Track {track.name} does not exist. Saving...")
            track.save(force_insert=True)
        return track

    @staticmethod
    def save_artist_track(artist: SpotifyArtist, track: SpotifyTrack):
        if not ArtistTrack.select().where(ArtistTrack.artist_id == artist.id, ArtistTrack.track_id == track.id).exists():
            logger.debug(f"Artist {artist.name} does not have track {track.name}. Adding...")
            ArtistTrack(artist_id=artist.id, track_id=track.id).save()
            logger.debug(f"Artist {artist.name} now has track {track.name}.")
        else:
            logger.debug(f"Artist {artist.name} already has track {track.name}.")

    @staticmethod
    def process_artist_item(item: dict, rank: int, request: SpotifyRequest) -> SpotifyArtist:
        artist = ItemProcessor.save_and_return_artist(item)
        logger.debug(f"Saving artist request {artist.name}")
        ArtistRequest(artist_id=artist.id,
                      request_id=request.id, rank=rank).save()
        logger.debug("Finished processing artists item")
        return artist

    @staticmethod
    def process_track_item(item: dict, rank: int, request: SpotifyRequest) -> list[SpotifyArtist]:
        track = ItemProcessor.save_and_return_track(item)
        song_artists = []
        for artist in item["artists"]:
            artist = ItemProcessor.save_and_return_artist(artist)
            song_artists.append(artist)
            ItemProcessor.save_artist_track(artist, track)
        logger.debug(f"Saving track request {track.name}")
        TrackRequest(track_id=track.id,
                     request_id=request.id, rank=rank).save()
        logger.debug("Finished processing tracks item")
        return song_artists
