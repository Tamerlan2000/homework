from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import json

Base = declarative_base()

class Indicator(Base):
    __tablename__ = 'indicators'
    id = Column(String, primary_key=True)
    date_first_seen = Column(String)
    date_last_seen = Column(String)
    deleted = Column(Boolean)
    description = Column(String, nullable=True)
    domain = Column(String)
    item_id = Column(String, ForeignKey('items.id'))

    def __repr__(self):
        return f"Indicator(id={self.id}, date_first_seen={self.date_first_seen}, date_last_seen={self.date_last_seen}, deleted={self.deleted}, description={self.description}, domain={self.domain})"


class Item(Base):
    __tablename__ = 'items'
    id = Column(String, primary_key=True)
    author = Column(String, nullable=True)
    company_id = Column(String)
    is_published = Column(Boolean)
    is_tailored = Column(Boolean)
    langs = Column(String)
    malware_list = Column(String)
    seq_update = Column(Integer)
    indicators = relationship('Indicator', backref='item')
    #data_id = Column(Integer, ForeignKey('data.id')) # New changes


    def __repr__(self):
        return f"Item(id={self.id}, author={self.author}, company_id={self.company_id}, is_published={self.is_published}, is_tailored={self.is_tailored}, langs={self.langs}, malware_list={self.malware_list}, seq_update={self.seq_update})"


class Data(Base):
    __tablename__ = 'data'
    #id = Column(Integer, primary_key=True)
    count = Column(Integer)
    seq_update = Column(Integer, primary_key=True)
    items = relationship('Item', backref='data')

    def __repr__(self):
        return f"Data(count={self.count}, seq_update={self.seq_update})"


class Parser():
    def __init__(self, json_string):
        json_data = json.loads(json_string)
        self.json_string = json_data
        #self.json_string = json_string

    def __parse_indicator(self, indicator_data: dict, item_id: str) -> Indicator:
        print('__parse_indicator')
        return Indicator(
            id=indicator_data['id'],
            date_first_seen=indicator_data['dateFirstSeen'],
            date_last_seen=indicator_data['dateLastSeen'],
            deleted=indicator_data['deleted'],
            description=indicator_data.get('description'),
            domain=indicator_data['domain'],
            item_id=item_id
        )

    def __parse_item(self, item_data: dict) -> Item:
        print('__parse_item')
        item = Item(
            id=item_data['id'],
            author=item_data.get('author'),
            company_id=",".join(item_data['companyId']),
            is_published=item_data['isPublished'],
            is_tailored=item_data['isTailored'],
            langs=",".join(item_data['langs']),
            malware_list=",".join(item_data['malwareList']),
            seq_update=item_data['seqUpdate']
        )
        for indicator_data in item_data['indicators']:
            indicator = self.__parse_indicator(indicator_data, item.id)
            item.indicators.append(indicator)
            print(item.__repr__())
        return item

    def __parse_data(self, json_data) -> Data:
        print('__parse_data')
        data_obj = Data(
            count=json_data.get('count'),
            seq_update=json_data.get('seqUpdate')
        )
        print('Data object is created')
        for item_data in json_data.get('items', []): #new change
            item = self.__parse_item(item_data)
            data_obj.items.append(item)
            print(data_obj.__repr__())
        return data_obj

    def parse_json(self) -> Data:
        #return self.__parse_data(self.json_string)
        json_data = json.loads(self.json_string)
        return self.__parse_data(json_data)
