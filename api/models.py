"""SQLAlchemy models for the API."""

# sqlalchemy imports
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from .database import Base

# Definition of the Movie model
class Movie(Base):
    """Movie model representing a movie record in the database."""

    __tablename__ = "movies" # nom de la table dans la base de donnee

    movieId = Column(Integer, primary_key=True, index=True) # id du film, cle primaire
    title = Column(String)# titre du film, comme difinit dans la table
    genres = Column(String)# genres du film, comme difinit dans la table

    #definition des relations avec les autres tables
    ratings = relationship("Rating", back_populates="movie", cascade="all, delete") # relation avec la table Rating
    links = relationship("Link", back_populates="movie", cascade="all, delete",uselist=False) # relation avec la table Link

# Definition of the Rating model
class Rating(Base):
    __tablename__ = "ratings"
    userId = Column(Integer, primary_key=True)
    movieId = Column(Integer, ForeignKey("movies.movieId"),primary_key=True)
    rating = Column(Float)
    timestamp = Column(Integer)
    #relation avec la table Movie
    movie = relationship("Movie", back_populates="ratings")


"""Definition of the Link model"""
class Tag(Base):
    __tablename__ = "tags"

    userId = Column(Integer, primary_key=True)
    movieId = Column(Integer, ForeignKey("movies.movieId"), primary_key=True)
    tag = Column(String, primary_key=True)
    timestamp = Column(Integer)
    #relation avec la table Movie
    movie = relationship("Movie", back_populates="tags")

    # Definition of the Link model
class Link(Base):
    __tablename__ = "links"

    movieId = Column(Integer, ForeignKey("movies.movieId"), primary_key=True)
    imdbId = Column(String)
    tmdbId = Column(String)

    #relation avec la table Movie
    movie = relationship("Movie", back_populates="links")
    