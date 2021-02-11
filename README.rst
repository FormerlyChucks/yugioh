======================
YGOPRODECK API Wrapper
======================

------------
Installation
------------

You can install it with pip3:

.. code-block:: bash

    pip3 install yugioh

-----
Usage
-----

Get card by name:

.. code-block:: python

    import yugioh
    
    card = yugioh.get_card(card_name = "The Wicked Dreadroot")
    print(card.name) #Returns "The Wicked Dreadroot"
    print(card.archetype) #Returns "Wicked God"
    print(card.attack) #Returns "4000"

Get card by ID:

.. code-block:: python

    import yugioh
    
    card = yugioh.get_card(card_id = "62180201")
    print(card.attack) #Returns "4000"
    print(card.name) #Returns "The Wicked Dreadroot"

All cards with `magician` in their name:

.. code-block:: python

    import yugioh

    cards = yugioh.get_cards_by_name(keyword = 'magician')
    for card in cards.list:
        print(card)

------------------
Monster Attributes
------------------

+--------------------+---------------------------------+
| Attribute          | Description                     |
+--------------------+---------------------------------+
| name               | The card's name                 |
+--------------------+---------------------------------+
| archetype          | The card's archetype            |
+--------------------+---------------------------------+
| attack             | The card's attack points        |
+--------------------+---------------------------------+
| attribute          | The card's attribute            |
+--------------------+---------------------------------+
| defense            | The card's defense points       |
+--------------------+---------------------------------+
| description        | The card's description          |
+--------------------+---------------------------------+
| id                 | The card's ID                   |
+--------------------+---------------------------------+
| level              | The card's level                |
+--------------------+---------------------------------+
| race               | The card's "race"               |
+--------------------+---------------------------------+
| type               | Monster/Normal card             |
+--------------------+---------------------------------+
| cardmarket_price   | The card's Cardmarket price     |
+--------------------+---------------------------------+
| tcgplayer_price    | The card's Tcgplayer price      |
+--------------------+---------------------------------+
| ebay_price         | The card's eBay price           |
+--------------------+---------------------------------+
| amazon_price       | The card's Amazon price         |
+--------------------+---------------------------------+
| ebay_price         | The card's eBay price           |
+--------------------+---------------------------------+
| coolstuffinc_price | The card's CoolStuffInc price   |
+--------------------+---------------------------------+

---------------------------
Spell/Trap/Skill Attributes
---------------------------

+--------------------+---------------------------------+
| Attribute          | Description                     |
+--------------------+---------------------------------+
| description        | The card's description          |
+--------------------+---------------------------------+
| id                 | The card's ID                   |
+--------------------+---------------------------------+
| name               | The card's name                 |
+--------------------+---------------------------------+
| type               | The card's type                 |
+--------------------+---------------------------------+
| race               | The card's "race"               |
+--------------------+---------------------------------+
| cardmarket_price   | The card's Cardmarket price     |
+--------------------+---------------------------------+
| tcgplayer_price    | The card's Tcgplayer price      |
+--------------------+---------------------------------+
| ebay_price         | The card's eBay price           |
+--------------------+---------------------------------+
| amazon_price       | The card's Amazon price         |
+--------------------+---------------------------------+
| ebay_price         | The card's eBay price           |
+--------------------+---------------------------------+
| coolstuffinc_price | The card's CoolStuffInc price   |
+--------------------+---------------------------------+

Please report all issues `here <https://github.com/ilikepyt/yugioh/issues>`_.
