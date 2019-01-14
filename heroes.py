from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Hero(Base):
    __tablename__ = 'heroes'

    id          = Column(Integer, primary_key=True)
    name        = Column(String)
    gender      = Column(String)
    eye_color   = Column(String)
    race        = Column(String)
    hair_color  = Column(String)
    height      = Column(Float)
    publisher   = Column(String)
    skin_color  = Column(String)
    alignment   = Column(String)
    weight      = Column(Float)

    def __repr__(self):
       base = ('<Hero(Id={0},name={1},Gender={2},Eye color={3},' + 
               'Race={4},Hair color={5},Height={6},Publisher={7},' + 
               'Skin color={8},Alignment={9},Weight={10})')
       return base.format(self.id          ,
                          self.name        ,
                          self.gender      ,
                          self.eye_color   ,
                          self.race        ,
                          self.hair_color  ,
                          self.height      ,
                          self.publisher   ,
                          self.skin_color  ,
                          self.alignment   ,
                          self.weight)