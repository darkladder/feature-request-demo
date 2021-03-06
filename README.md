# Feature Request App Demo

@see https://github.com/IntuitiveWebSolutions/EngineeringMidLevel

## Description

A "feature request" is a request for a new feature that will be added onto an existing piece of software. Assume that the user is an employee at IWS who would be entering this information after having some correspondence with the client that is requesting the feature. The necessary fields are:

- **Title:** A short, descriptive name of the feature request.
- **Description:** A long description of the feature request.
- **Client:** A selection list of clients (use "Client A", "Client B", "Client C")
- **Client Priority:** A numbered priority according to the client (1...n). Client Priority numbers should not repeat for the given client, so if a priority is set on a new feature as "1", then all other feature requests for that client should be reordered.
- **Target Date:** The date that the client is hoping to have the feature.
- **Product Area:** A selection list of product areas (use 'Policies', 'Billing', 'Claims', 'Reports')

## Prerequisites

- Docker
- Docker Compose
